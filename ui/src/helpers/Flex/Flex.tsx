import { CSSProperties } from "react";
import styled, { CSSObject } from "styled-components";

export interface FlexProps {
  $customStyle?: CSSObject | CSSProperties;
}

const Flex = styled.div<FlexProps>`
  display: flex;

  ${({ $customStyle }) => ({ ...$customStyle })}
`;

export { Flex };
